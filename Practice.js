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


















let myVar = myFunc(a, b) {
    .
};

let myVar = (a, b) {
    .
};

let myVar = (a, b) => ;

let myVar = (a) => {
    .
};

console.log(myVar(3, 2));

let myVar = [2, 4, 6, 8];

console.log(myArray.map(currentElement => currentElement * 2));

[4, 8, 12, 16]

console.log(myArray.map((currentElement, index) => {
    return `Current Element at index [ ${index} ] is [ ${currentElement} ]`;
}));

['Current Element at index [ 0 ] is [ 2 ]', 'Current Element at index [ 1 ] is [ 4 ]', 'Current Element at index [ 2 ] is [ 6 ]', 'Current Element at index [ 3 ] is [ 8 ]']



What works and what not?

a-   When using arrow functions within another functions, do not forget to use return keyword if {} braces are used.
    Because if return is skipped in this case, the function will return undefined.
b-   When using arrow functions, necessarily skip using return keyword if {} braces are themselves skipped.
c-   When using arrow functions within another functions, you can include multiple statements with semicolons.

class App {
    constructor (name, age) {
        this.name = name;
        this.age = age;
    }
}
