package
src_4;
import java.util.ArrayList;

public


class Main {
public static long[] solution(long[] remittance) {
long[] answer = {};
ArrayList < Long > result = new ArrayList <> ();

for (long number: remittance

) {
    String
target_number = getHalf(number);
int
decimal = String.valueOf(number).length() / 2;

long
palindrome = getPalindrome(target_number);
long
temp_result = palindrome;

while (palindrome < number) {
target_number = String.valueOf(Integer.parseInt(target_number) + (int) Math.pow(10, decimal));
palindrome = getPalindrome(target_number);
temp_result = palindrome;
}

result.add(temp_result);
}

answer = result.stream().mapToLong(Long::longValue).toArray();
return answer;
}

private
static
long
getPalindrome(String
target) {
String
half = target.substring(0, target.length() / 2);

if (target.length() % 2 == 1) {
return Integer.parseInt(target.substring(0, target.length() / 2 + 1) + new
StringBuilder(half).reverse().toString());
} else {
return Integer.parseInt(target.substring(0, target.length() / 2) + new
StringBuilder(half).reverse().toString());
}
}

private
static
String
getHalf(long
target) {
    String
target_str = String.valueOf(target);
int
n = target_str.length();
int
m = n / 2;

if (n % 2 == 1)
{
return target_str.substring(0, n / 2 + 1) + "0".repeat(m);
} else {
return target_str.substring(0, n / 2) + "0".repeat(m);
}
}

public
static
void
main(String[]
args) {
    long[]
remittance = {1, 102, 10, 99, 100};
long[]
answer = solution(remittance);

for (int i = 0; i < answer.length; i++)
{
System.out.println("answer[i] = " + answer[i]);
}
}
}