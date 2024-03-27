type Fn = (n: number, i: number) => any

function filter(arr: number[], fn: Fn): number[] {
    const resultArr = []
    
    for (let i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            resultArr.push(arr[i])
        }
    }
    
    return resultArr
};