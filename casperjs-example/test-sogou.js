casper.test.begin('test sogou.com search engine', 3, function suite(test) {
    casper.start("https://www.sogou.com/", function() {
        test.assertExists('#sf', "locate search form");
        this.fill('#sf', {
            query: "casper+e2e+test"
        }, true);
    });

    casper.then(function() {
        this.captureSelector('searchresult.png', 'html');
        test.assertUrlMatch(/query=casper\+e2e\+test/, "search term has been submitted");
        test.assertEval(function() {
            return __utils__.findAll("h3.pt").length >= 1;
        }, "sogou search for \"casper\" retrieves 1 or more results");
    });

    casper.run(function() {
        test.done();
    });
});
