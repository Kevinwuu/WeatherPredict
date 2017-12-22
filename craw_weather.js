var request = require('request');
var cheerio = require('cheerio');

request("http://e-service.cwb.gov.tw/HistoryDataQuery/DayDataController.do?command=viewMain&station=466900&stname=%25E6%25B7%25A1%25E6%25B0%25B4&datepicker=2017-12-05", function (error, response, body) {
	if (!error) {
		var $ = cheerio.load(body);
		//擷取標題
		var title = $('tbody > .first_tr');
		console.log("<"+title.find('th:nth-child(3)').text()+">");

		//擷取數據
		var value = $('tbody > tr ');
		// console.log(value.find('td:nth-child(3)').text());
		value.each(function() {
			console.log($(this).find('td:nth-child(4)').text());
		});
	} else {
		console.log("擷取錯誤：" + error);
	}
});
