---
name: tavily
description: Search the web using Tavily API. Optimized for LLMs with concise, factual results.
metadata:
  openclaw:
    requires:
      node: 18+
    env:
      TAVILY_API_KEY: "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"
---

# Tavily Search

Performs a web search using the Tavily API.

## Usage

```javascript
// Search for "current events"
search("current events");

// Advanced search
search("python tutorials", {
  search_depth: "advanced", // basic | advanced
  max_results: 5,
  include_answer: true,
  include_raw_content: false,
  include_domains: ["python.org", "realpython.com"],
  exclude_domains: ["reddit.com"]
});
```

## Tools

### tavily_search

Search the web and return relevant results.

- `query` (string, required): The search query.
- `options` (object, optional):
  - `search_depth` (string): "basic" or "advanced" (default: "basic").
  - `topic` (string): "general" or "news".
  - `max_results` (number): Max results to return (default: 5).
  - `include_answer` (boolean): Include a short answer summary.
  - `include_raw_content` (boolean): Include full raw content.
