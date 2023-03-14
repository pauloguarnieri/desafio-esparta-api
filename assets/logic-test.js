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

//sera passado um array com quantidade impar, um elemento do array nao tera par
//retornar o valor que não tem um par no array

function array(A) {

    let objectCounter = arrayCounter(A);

    for (key in objectCounter) {
        if (objectCounter[key] % 2 != 0) {
            return key;
        }
    }

};

console.log(array(arrayTest));


let arrayTest2 = [2, 1, 1, 2, 3, 1] // --> 3 valores diferentes

//retorna o numero de valores diferentes no array

function distinct(A) {

    let objectCounter = arrayCounter(A);

    return Object.keys(objectCounter).length;
};

console.log(distinct(arrayTest2));

function euclidean(N, M) {

    let counter = 0
    let arrayOfEatedChocolates = []
    while (!arrayOfEatedChocolates.includes(counter)) {
        if (counter > N - 1) {
            counter -= N
            continue
        }
        arrayOfEatedChocolates.push(counter);
        counter += M
    }
    console.log(arrayOfEatedChocolates)
    return arrayOfEatedChocolates.length
}

console.log(euclidean(10, 4));