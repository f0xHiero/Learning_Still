/**
 *Submitted for verification at FtmScan.com on 2021-03-17
*/

//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.7.0;

contract countingGame {
    
    /* Ok Gang, here's the most basic bullshit game I could imagine. 
    Enjoy playing what is essentially 'click-of-war' V 0.1.0
    */

    int256 count = count;
    
    constructor() {
        count = 0;
    }
    
    function getCount() public view returns(int256){
        return count;
    }
    
    function addOneToTheCount() public {
        count = count + 1;
    }
    
    function subtractOneFromTheCount() public {
        count = count - 1;
    }
}
