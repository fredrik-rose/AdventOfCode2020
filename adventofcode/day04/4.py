# Day 4: Passport Processing
import re


def parse_input(file_path):
    def parse_passport(text):
        return dict([e.split(':') for e in re.split(r' |\n', text)])

    with open(file_path) as file:
        text = file.read()
        passports = [parse_passport(e) for e in text.rstrip().split('\n\n')]
        return passports


def part_one(passports):
    valid_passports = count_valid_passports(passports, validate_passport_part_one)
    print("There are {} valid passports in part one.".format(valid_passports))


def validate_passport_part_one(passport):
    required_fields = set(('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))
    return len(required_fields - set(passport.keys())) == 0


def count_valid_passports(passports, validator):
    return sum(validator(p) for p in passports)


def part_two(passports):
    valid_passports = count_valid_passports(passports, validate_passport_part_two)
    print("There are {} valid passports in part two.".format(valid_passports))


def validate_passport_part_two(passport):
    try:
        hgt = re.match(r'(\d+)(cm|in)$', passport['hgt'])
        height = int(hgt.group(1))
        unit = hgt.group(2)
        valid_hgt = (150 <= height <= 193) if unit == 'cm' else (59 <= height <= 76)
        return (1920 <= int(passport['byr']) <= 2002 and
                2010 <= int(passport['iyr']) <= 2020 and
                2020 <= int(passport['eyr']) <= 2030 and
                valid_hgt and
                bool(re.match(r'#[0-9a-f]{6}$', passport['hcl'])) and
                bool(re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$', passport['ecl'])) and
                bool(re.match(r'[\d]{9}$', passport['pid'])))
    except (KeyError, AttributeError):
        return False


def main():
    passports = parse_input('4.txt')
    part_one(passports.copy())
    part_two(passports.copy())


if __name__ == "__main__":
    main()
