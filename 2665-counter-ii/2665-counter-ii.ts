type Counter = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): Counter {
    let curr = init
    
    function increment() {
        return ++curr
    }
    
    function decrement() {
        return --curr
    }
    
    function reset() {
        curr = init
        return curr
    }
    
    return {
        increment, 
        decrement,
        reset
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */