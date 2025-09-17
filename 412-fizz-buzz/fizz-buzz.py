class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        for i in range(n):
            print(i)
            num = i + 1
            if num % 3 == 0 and num % 5 == 0:
                ret.append("FizzBuzz")
            elif num % 3 == 0:
                ret.append("Fizz")
            elif num % 5 == 0:
                ret.append("Buzz")
            else:
                ret.append(str(num))
        return ret



        