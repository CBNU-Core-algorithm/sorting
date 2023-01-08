use std::collections::HashMap;

fn main() {
    let min_sick_lang = [
        ("ng", "L"),
        ("a", "A"),
        ("b", "B"),
        ("k", "C"),
        ("d", "D"),
        ("e", "E"),
        ("g", "F"),
        ("h", "G"),
        ("i", "H"),
        ("l", "I"),
        ("m", "J"),
        ("n", "K"),
        ("o", "M"),
        ("p", "N"),
        ("r", "O"),
        ("s", "P"),
        ("t", "Q"),
        ("u", "R"),
        ("w", "S"),
        ("y", "T"),
    ];

    let n = input().parse().unwrap();

    let mut mswords: Vec<String> = Vec::new();
    for _ in 0..n {
        mswords.push(input());
    }

    let mut word_pair: Vec<(String, String)> = Vec::new();
    for word in mswords {
        let mut origin = (&*word).to_string();
        for (key, value) in min_sick_lang {
            origin = origin.replace(key, value);
        }
        // println!("{} -> {}", word, origin);
        word_pair.push((word, origin));
    }

    // println!("{:?}", word_pair);
    word_pair.sort_by(|a,b| a.1.cmp(&b.1));
    // println!("{:?}", word_pair);
    for val in word_pair {
        println!("{}", val.0);
    }
}

fn input() -> String {
    let mut buf = String::new();
    std::io::stdin()
        .read_line(&mut buf)
        .expect("Failed to Read Line");
    buf.trim().to_string()
}
