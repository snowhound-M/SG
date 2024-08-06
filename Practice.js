function myFunction(x, y) {
    console.log(x + y);
}

myFunction(3, 4);

function myFunction(x, y) {
    return x + y;
}

let newReturnValue = myFunction(3, 4);
console.log(newReturnValue);

let returnValue = function myFunction(x, y) {
    console.log(x + y);
};

returnValue(3, 4);


let returnValue = (x, y) => {
    console.log(x + y);
};

/*

let returnValue = (x, y) => console.log(x + y);
};

*/

returnValue(3, 4);



