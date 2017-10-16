

const puppeteer = require('puppeteer');
const devices = require('puppeteer/DeviceDescriptors');
//const nexus = devices['Nexus 10 landscape'];

(async () => {
  const browser = await puppeteer.launch({headless: true});
  const page = await browser.newPage();
  await page.goto('https://studentportal.nackademin.se/mod/assign/view.php?id=39442&action=grading',{waitUntil: 'networkidle'});
  //await page.emulate(nexus);
  await page.focus ('#username');
  await page.type('USERNAME', {delay: 10});
  await page.focus ('#password');
  await page.type('PASSWORD', {delay: 10}); 
  await page.click('#loginbtn');
  await page.waitForSelector('#id_submit',{waitUntil: 'networkidle'});
  await page.evaluate(() => {
	document.getElementsByClassName('moveto')[0].click();
  })
  await page.waitFor(4000);

  await page.screenshot({path: 'assignment1_now.jpeg', omitBackground:true ,quality:100, fullPage: true});

  /*await page.screenshot({
	path: 'assignment1_now.jpg', 
	quality:100, 
	//fullPage: true, 
	clip: {x:0,y:0, width:400, height:800},
	});
*/
  browser.close();
})();





















