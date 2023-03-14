function solution(N, M) {

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

console.log(solution(10, 4));