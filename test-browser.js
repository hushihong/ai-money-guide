const puppeteer = require('puppeteer-core');
const fs = require('fs');

(async () => {
  console.log('Starting browser test...');
  try {
    const browser = await puppeteer.launch({
      executablePath: '/usr/bin/google-chrome',
      headless: true,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    
    const page = await browser.newPage();
    console.log('Navigating to example.com...');
    await page.goto('https://example.com');
    
    const title = await page.title();
    console.log(`Page title: ${title}`);
    
    console.log('Taking screenshot...');
    await page.screenshot({ path: 'example.png' });
    
    await browser.close();
    console.log('Test complete. Screenshot saved to example.png');
  } catch (err) {
    console.error('Error:', err);
  }
})();
