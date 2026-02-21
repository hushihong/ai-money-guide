#!/usr/bin/env node

const https = require('https');

const API_KEY = process.env.TAVILY_API_KEY || "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";

if (!API_KEY) {
  console.error("Error: TAVILY_API_KEY environment variable not set.");
  process.exit(1);
}

const args = process.argv.slice(2);
if (args.length === 0) {
  console.error("Usage: tavily_search <query> [options-json]");
  process.exit(1);
}

const query = args[0];
let options = {};
if (args[1]) {
  try {
    options = JSON.parse(args[1]);
  } catch (e) {
    // ignore
  }
}

const body = JSON.stringify({
  api_key: API_KEY,
  query: query,
  search_depth: options.search_depth || "basic",
  topic: options.topic || "general",
  max_results: options.max_results || 5,
  include_answer: options.include_answer || false,
  include_raw_content: options.include_raw_content || false,
  include_domains: options.include_domains || [],
  exclude_domains: options.exclude_domains || []
});

const req = https.request({
  hostname: 'api.tavily.com',
  path: '/search',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': body.length
  }
}, (res) => {
  let data = '';
  res.on('data', (chunk) => { data += chunk; });
  res.on('end', () => {
    try {
      if (res.statusCode !== 200) {
        console.error(`Error: Tavily API returned ${res.statusCode}: ${data}`);
        process.exit(1);
      }
      const json = JSON.parse(data);
      // Simplify output for LLM consumption
      const output = {
        query: json.query,
        answer: json.answer,
        results: json.results.map(r => ({
          title: r.title,
          url: r.url,
          content: r.content,
          score: r.score,
          published_date: r.published_date
        }))
      };
      console.log(JSON.stringify(output, null, 2));
    } catch (e) {
      console.error(`Error parsing response: ${e.message}`);
      process.exit(1);
    }
  });
});

req.on('error', (e) => {
  console.error(`Request error: ${e.message}`);
  process.exit(1);
});

req.write(body);
req.end();
