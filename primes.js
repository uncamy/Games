#!/usr/bin/env node
var fs = require('fs')
var outfile = "primes1.txt";

var prime = function(n){
	if (n<2){return false;}
	var q = Math.sqrt(n);
	for (i=2; i <=(Math.floor(q)); i++){
		if (n%i ==0){return false;}
	}
	return n;
}

var firstkprime = function(k) {
	var arr = [];
	var i = 1;
	while (arr.length<k){ 	
		if (prime(i) !== false){
			arr.push(prime(i));
			}
		i++;
		};
	return arr;
};
var fmt = function(arr) {
	return arr.join(",");
};
var k = 100;
var out = fmt(firstkprime(k));
fs.writeFileSync(outfile, out);
console.log("Script: " + __filename + "\nWrote: " + out + "To: " + outfile);

