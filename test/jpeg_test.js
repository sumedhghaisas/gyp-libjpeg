'use strict';
var libjpeg = require('./build/Release/jpeg_test');
var expect = require('chai').expect;

describe('functionality', function() {

    describe('to_jpeg_test', function() {

        it('should be able to convert primary images to jpeg images', function() {
            var result = libjpeg.toJpeg('../libjpeg/testimg.bmp', 'testimg.jpeg');
            expect(result).to.eql(1);
        });
    });
});
