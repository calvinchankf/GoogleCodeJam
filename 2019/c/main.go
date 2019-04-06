package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func getPrimes(n int) []int {
	if n < 2 {
		return []int{}
	}
	notPrime := make(map[int]bool)
	res := []int{}
	for i := 2; i < n; i++ {
		_, e := notPrime[i]
		if !e {
			res = append(res, i)
			for j := 2; i*j < n; j++ {
				notPrime[i*j] = true
			}
		}
	}
	return res
}

func bsearch(arr []int, target int) int {
	min := 0
	max := len(arr) - 1
	for min <= max {
		mean := (min + max) / 2
		if target == arr[mean] {
			return mean
		} else if target > arr[mean] {
			min = mean + 1
		} else if target < arr[mean] {
			max = mean - 1
		}
	}
	return -1
}

func cryptopangram(n int, nums []int) string {
	primes := getPrimes(n + 1)
	alphabets := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	if len(nums) == 0 {
		return ""
	}
	first := nums[0]
	i := 0
	buffer := 0.0
	for i < len(primes) {
		buffer = float64(first) / float64(primes[i])
		if buffer != float64(int64(buffer)) {
			i++
		} else {
			break
		}
	}

	indeces := []int{}
	firstNum := primes[i]

	firstIdx := bsearch(primes, firstNum)
	indeces = append(indeces, firstIdx)

	buffero := int(buffer)

	bufferIdx := bsearch(primes, buffero)
	indeces = append(indeces, bufferIdx)

	// fmt.Println(firstNum, buffero)

	for i := 1; i < len(nums); i++ {
		num := nums[i]
		buffero = num / buffero
		bufferIdx = bsearch(primes, buffero)
		indeces = append(indeces, bufferIdx)
	}

	// fmt.Println(indeces)

	indexSet := make(map[int]bool)
	for _, idx := range indeces {
		indexSet[idx] = true
	}

	sortedIndeces := []int{}
	for key := range indexSet {
		sortedIndeces = append(sortedIndeces, key)
	}
	sort.Ints(sortedIndeces)

	res := ""
	for _, pIdx := range indeces {
		pos := bsearch(sortedIndeces, pIdx)
		res += string(alphabets[pos])
	}

	return res
}

func main() {
	// fmt.Println(getPrimes(100))

	// a := []int{
	// 	217, 1891, 4819, 2291, 2987,
	// 	3811, 1739, 2491, 4717, 445,
	// 	65, 1079, 8383, 5353, 901,
	// 	187, 649, 1003, 697, 3239,
	// 	7663, 291, 123, 779, 1007,
	// 	3551, 1943, 2117, 1679, 989,
	// 	3053,
	// }
	// fmt.Println(cryptopangram(103, a))

	var input int
	fmt.Scanln(&input)

	scanner := bufio.NewScanner(os.Stdin)
	i := 1
	n := 0
	for scanner.Scan() && i <= input {
		line := scanner.Text()
		rawNums := strings.Fields(line)
		if len(rawNums) == 2 {
			n, _ = strconv.Atoi(rawNums[0])
		} else {
			nums := []int{}
			for _, raw := range rawNums {
				num, _ := strconv.Atoi(raw)
				nums = append(nums, num)
			}
			s := cryptopangram(n, nums)
			fmt.Printf("Case #%d: %s\n", i, s)
			i++
		}
	}

	// for i := 1; i <= input; i++ {
	// 	// 1st line
	// 	scanner.Scan() // use `for scanner.Scan()` to keep reading
	// 	line1 := scanner.Text()
	// 	rawNums1 := strings.Fields(line1)
	// 	n, _ := strconv.Atoi(rawNums1[0])

	// 	// 2nd line
	// 	scanner.Scan() // use `for scanner.Scan()` to keep reading
	// 	line2 := scanner.Text() + "\n"
	// 	rawNums2 := strings.Fields(line2)
	// 	nums := []int{}
	// 	for _, raw := range rawNums2 {
	// 		num, _ := strconv.Atoi(raw)
	// 		nums = append(nums, num)
	// 	}

	// 	s := cryptopangram(n, nums)
	// 	fmt.Printf("Case #%d: %s\n", i, s)
	// }
}
