console.log("Sudoku verifier");
var solved1 = "217386954356194728489257136165948273872563419943712685521439867798625341634871592"

var sudoku = [];
var k = 0;
for(var i = 0; i<9; i++){
    var row = [];
    for(var j = 0; j<9; j++){
        row.push(Number(solved1[k]));
        k = k + 1;
    }
    sudoku.push(row);
}
console.log(sudoku);

var vertSumFlag = true;
var horiSumFlag = true;
var blockSumFlag = true;
// Vertical sum and Horizontal sum check
for(var i = 0; i<9; i++){
    var horiSum = 0;
    var veriSum = 0;
    var blockSum = 0;
    for(var j = 0; j<9; j++){
        horiSum = horiSum + sudoku[i][j];
        veriSum = veriSum + sudoku[j][i];
        // console.log(Math.floor((i/3)*3 + j/3), Math.floor((i*3)%9 + j%3));
        blockSum = blockSum + sudoku[Math.floor(i/3)*3 + Math.floor(j/3)][(i*3)%9 + j%3];
    }
    // console.log(veriSum, horiSum, blockSum);
    veriSumFlag = (veriSum == 45)? true : false;
    horiSumFlag = (horiSum == 45)? true : false;
    blockSumFlag = (blockSum == 45)? true : false;
    if(!vertSumFlag && !horiSumFlag && !blockSumFlag){
        console.log("Not Valid");
        return "Not Valid";
    }
}
console.log("Valid");
return "Valid";



