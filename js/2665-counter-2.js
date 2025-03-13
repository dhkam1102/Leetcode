/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let original = init;
    let current = init;

    function increment(){
        return ++current;
    }
    function decrement(){
        return --current;
    }
    function reset(){
        current = original;
        return current;
    }

    return {increment, decrement, reset}
    // return { increment: increment, decrement: decrement, reset: reset };

};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */