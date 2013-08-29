#!/usr/bin/env node

/* this program aims to pull down a list of urls, process them async
 and make a list of agencies by parent_id*/


var request = require('request');
var async = require('async');
var uu =require('underscore');

/* 2. Parse data and pull out parent_id */
function agen_data2agenName_parentId(agen_data){
    var notUndefined = function(xx) {return !uu.isUndefined(xx);};
    var agenName = uu.filter(uu.pluck(agen_data, 'name'), notUndefined);
    var parentId = uu.filter(uu.pluck(agen_data, 'parent_id'), notUndefined);

    return {'agenName': agenName, 'parentId': parentId};
}

function agen_datas2parentId_to_names(agen_datas, cb){
    log(agen_datas);
    log(arguments.callee.name);
    agenName_parentId =  uu.map(agen_datas, agen_data2agenName_parentId);
    var parentId_to_names = {};
    for(var ii in agenName_parentId){
	var ms = agenName_parentId[ii];
	var nm = ms.agenName;
	if(uu.has(parentId_to_names, ms.parentId)) {
	    parentId_to_names[ms.parentId].push(nm);
	} else {
	    parentId_to_names[ms.parentId] = [nm];
	}
    }
    cb(null, parentId_to_names);
}


/* 3. Download agency URLs and convert JSON to internal data */
function agen_url2agen_data(agen_url, cb) {
    log(arguments.callee.name);
    var err_resp_body2agen_data = function(err, resp, body) {
	if(!err && resp.statusCode == 200) {
	    var agen_data = JSON.parse(body);
	    cb(null, agen_data);
	}
     };
     request(agen_url, err_resp_body2agen_data);
}

//apply function in parallel to all agen_urls and send to callback
function agen_urls2agen_datas(agen_urls, cb) {
    log(arguments.callee.name);
    var num_simultaneous_downloads =50;
    async.mapLimit(agen_urls,num_simultaneous_downloads,  agen_url2agen_data, cb);
}

/* 4. Bring in parsed data from URL to create agency URLs */
function register_data2agen_urls(register_data, cb) {
    log(arguments.callee.name);
    var notUndefined = function(xx) {return !uu.isUndefined(xx);};
    var agen_urls = uu.filter(uu.pluck(register_data, 'json_url'), notUndefined);
    cb(null, agen_urls);
}

/* 5. Pull down the body and parse JSON into a data structure (register_data) */
function register_url2register_data(register_url, cb){
    log(arguments.callee.name);
    var err_resp_body2register_data = function(err, resp, body) {
	if (!err && resp.statusCode == 200) {
	    var register_data = JSON.parse(body);
	    cb(null, register_data);
	    }
    };
    request(register_url, err_resp_body2register_data);
}

/*bringing it together w/ async compose*/
function parentId_to_names2console(err, parentId_to_names) {
    log(arguments.callee.name);
    console.log(JSON.stringify(parentID_to_names, null, 2));
}
//forces all request to complete before subsequence code was executed
var register_url2console = async.compose(agen_datas2parentId_to_names,
					 agen_urls2agen_datas,
					 register_data2agen_urls,
					 register_url2register_data);

var register_url = "https://www.federalregister.gov/api/v1/agencies.json";
register_url2console(register_url,parentId_to_names2console);
