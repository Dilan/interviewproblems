var findUnique = require('../InterviewCake-Problem-21').findUnique;

// tests:
(function() {
  assertEquals(findUnique([1,2,3,5,3,2,1]), 5);
})();

function assertEquals(a, b) {
  console.log(
    (a.toString() !== b.toString()) ? 'test fail: (' + a + ') !== (' + b + ')' : 'test pass.'
  );
}