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


let arrayTest2 = [2, 1, 1, 2, 3, 1]


function distinct(A) {

    let objectCounter = arrayCounter(A);

    return Object.keys(objectCounter).length;
};

console.log(distinct(arrayTest2));