fn count_positives_sum_negatives(input: Vec<i32>) -> Vec<i32> {
    if input.len() > 0 {
        let mut count_positives = 0;
        let mut sum_negatives = 0;

        for number in &input {
            if number > &0 {
                count_positives += 1
            } else if number < &0 {
                sum_negatives += number
            }
        }

        [count_positives, sum_negatives].to_vec()
    } else {
        [].to_vec()
    }
}
