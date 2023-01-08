fn main() {
    let n = {
        let mut buf = String::new();
        std::io::stdin().read_line(&mut buf).unwrap();
        buf.trim().parse().unwrap()
    };

    let mut times: Vec<(u32, u32)> = Vec::new();
    for _ in 0..n {
        times.push({
            let mut buf = String::new();
            std::io::stdin().read_line(&mut buf).unwrap();

            let tup: (u32, u32) = {
                let mut a: Vec<u32> = Vec::new();
                for string in buf.trim().split(' ') {
                    a.push(string.parse().unwrap());
                }
                (a[0], a[1])
            };

            tup
        });
    }

    times.sort_by(|a, b| a.1.cmp(&b.1));
    // println!("{:?}", times);

    let mut cnt = 1u32;
    let mut cur = times[0].1;
    // println!("[+] 회의 진행 {}시부터 {}시까지", times[0].0, times[0].1);
    for tup in times {
        // println!(
        //     "[+] 이전 회의는 {}시에 끝났다. {}시에 시작이 가능한가?",
        //     cur, tup.0
        // );
        if tup.0 >= cur {
            // println!("    Yes");
            cur = tup.1;
            cnt += 1;
        } else {
            // println!("    No\n");
        }
    }

    println!("{}", cnt);
}
