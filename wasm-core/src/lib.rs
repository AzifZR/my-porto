// Pure Rust functions compiled directly to WebAssembly (WASM)
// Zero external dependencies, pure binary execution in browser

#[no_mangle]
pub extern "C" fn rust_fibonacci(n: u32) -> u64 {
    if n <= 1 {
        return n as u64;
    }
    let mut a: u64 = 0;
    let mut b: u64 = 1;
    for _ in 2..=n {
        let temp = a.wrapping_add(b);
        a = b;
        b = temp;
    }
    b
}

#[no_mangle]
pub extern "C" fn rust_count_primes(limit: u32) -> u32 {
    let mut count = 0;
    for i in 2..=limit {
        let mut is_prime = true;
        let mut d = 2;
        while d * d <= i {
            if i % d == 0 {
                is_prime = false;
                break;
            }
            d += 1;
        }
        if is_prime {
            count += 1;
        }
    }
    count
}

#[no_mangle]
pub extern "C" fn rust_checksum(val: u32) -> u32 {
    let mut hash = 0x811c9dc5u32;
    for b in val.to_le_bytes() {
        hash ^= b as u32;
        hash = hash.wrapping_mul(0x01000193);
    }
    hash
}
