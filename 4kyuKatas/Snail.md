# Snail Sort
:computer: Join [CodeWars](www.codewars.com/r/v0KX6w) and :point_right: follow [me](https://www.codewars.com/users/gmarte)!

Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
```
array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
```
For better understanding, please follow the numbers of the next array consecutively:

```
array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
```
This image will illustrate things more clearly:

![image](http://www.haan.lu/files/2513/8347/2456/snail.png)

##### NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

##### NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].

<details><summary>open to view solution</summary>

### Solution
```python
def snail(snail_map):
    listResult = list()
    while (snail_map):
        listResult.append(snail_map.pop(0))
        snail_map = list(map(list, zip(*snail_map)))[::-1]
    return [x for i in listResult for x in i]
```    
</details>