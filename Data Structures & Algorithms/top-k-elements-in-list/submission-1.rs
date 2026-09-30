use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if k <= 0 {
            return Vec::new();
        }

        let k = k as usize;
        let mut num_count: HashMap<i32, usize> = HashMap::new();
        let mut unique_nums: Vec<i32> = Vec::new();
        let mut top_k_num: Vec<i32> = Vec::new();

        // Insert a number while keeping frequencies in descending order.
        fn insert_num(
            num: i32,
            top_k_num: &mut Vec<i32>,
            num_count: &HashMap<i32, usize>,
        ) {
            for i in 0..top_k_num.len() {
                if num_count[&num] > num_count[&top_k_num[i]] {
                    top_k_num.insert(i, num);
                    return;
                }
            }

            top_k_num.push(num);
        }

        fn update_top_k(
            num: i32,
            top_k_num: &mut Vec<i32>,
            num_count: &HashMap<i32, usize>,
            k: usize,
        ) {
            if top_k_num.len() < k {
                insert_num(num, top_k_num, num_count);
            } else {
                // The vector is nonempty because k > 0.
                let last_num = top_k_num[top_k_num.len() - 1];

                if num_count[&num] > num_count[&last_num] {
                    top_k_num.pop();
                    insert_num(num, top_k_num, num_count);
                }
            }
        }

        // Count frequencies and preserve the order of first appearance.
        for num in nums {
            let count = num_count.entry(num).or_insert(0);

            if *count == 0 {
                unique_nums.push(num);
            }

            *count += 1;
        }

        for num in unique_nums {
            update_top_k(num, &mut top_k_num, &num_count, k);
        }

        top_k_num
    }
}