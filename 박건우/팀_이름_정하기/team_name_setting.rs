use std::collections::HashMap;
use std::io;

fn main() {
    let mut name = String::new();
    let mut n: String = String::new();
    let mut team_name: Vec<String> = Vec::new();
    let mut hmap: HashMap<u32, Vec<String>> = HashMap::new();

    io::stdin().read_line(&mut name).unwrap();
    let name_love = find_digits(&name);

    io::stdin().read_line(&mut n).unwrap();
    let n: usize = n.trim().parse().unwrap();

    for _ in 0..n {
        let mut buf = String::new();
        io::stdin().read_line(&mut buf).unwrap();
        team_name.push(buf.trim().to_string());
    }

    team_name.sort();

    for element in team_name {
        let love = {
            let a = find_digits(&element);
            (a.0 + name_love.0, a.1 + name_love.1, a.2 + name_love.2, a.3 + name_love.3)
        };
        hmap.entry(
            (love.0 + love.1)
                * (love.0 + love.2)
                * (love.0 + love.3)
                * (love.1 + love.2)
                * (love.1 + love.3)
                * (love.2 + love.3)
                % 100,
        )
            .or_insert({
                let vec: Vec<String> = Vec::new();
                vec
            })
            .push(element);
        println!("{:#?}", hmap);
    }
}

fn find_digits(string: &String) -> (u32, u32, u32, u32) {
    let mut love = (0, 0, 0, 0);
    for ch in string.chars() {
        match ch {
            'L' => love.0 += 1,
            'O' => love.1 += 1,
            'V' => love.2 += 1,
            'E' => love.3 += 1,
            _ => (),
        }
    }
    love
}
