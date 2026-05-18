#[unsafe(no_mangle)]
pub extern "C" fn sum_of_squares(limit: u64) -> u64 {
    let mut total = 0;

    for i in 0..limit {
        total += i * i;
    }

    total
}