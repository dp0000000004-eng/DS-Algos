function medianOfSortedArray(nums1, nums2) {


    const marged_nums = [...nums1, ...nums2]
    const ans = marged_nums[0]

    console.log(marged_nums)
    const sum = marged_nums.reduce((acc, num) => acc + num, 0)

    if (marged_nums.length % 2 === 0) {
        if (sum != 0 && marged_nums.length > 1) {
            ans = (marged_nums.length / 2 ) + 0.5
        }
    }else if (marged_nums.length % 2 != 0) {
        if ( sum != 0 && marged_nums.length > 1 ) {
            ans =  sum / marged_nums.length
        }
    }

    return ans

}

const nums1 = []
const nums2 = [1]

console.log(medianOfSortedArray(nums1, nums2))