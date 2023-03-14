function arrayCounter(list) {

    const objectCounter = {};

    for (let i = 0; i < list.length; i++) {
        let actualNumber = list[i];

        if (objectCounter[actualNumber] === undefined) {
            objectCounter[actualNumber] = 1;
        } else {
            objectCounter[actualNumber] += 1;
        }
    }

    return objectCounter;

}


let arrayTest = [9, 3, 9, 3, 9, 7, 9]


function solution(A) {

    let objectCounter = arrayCounter(A);

    for (key in objectCounter) {
        if (objectCounter[key] % 2 != 0) {
            return key;
        }
    }

};

console.log(solution(arrayTest));




