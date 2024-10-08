public class PalindromeChecker {

    public static boolean isPalindrome(String s) {

        // StringBuilder para armazenar a string "limpa"
        StringBuilder cleanedString = new StringBuilder();

        // Itera sobre cada caractere da string original
        for (char c : s.toCharArray()) {

            // Verifica se é um caractere alfanúmerico
            if (Character.isLetterOrDigit(c)) {
                // Adiciona a string "limpa" em letras minusculas
                cleanedString.append(Character.toLowerCase(c));
            }
        }

        // Converte o StringBuilder em string final
        String cleaned = cleanedString.toString();

        // Verifica se a string "limpa" é igual a sua versão reversa
        String reversed = cleanedString.reverse().toString();

        return cleaned.equals(reversed);

    }

    public static void main(String[] args) {
        // Testes com exemplos
        String s1 = "A man, a plan, a canal: Panama";
        String s2 = "race a car";

        System.out.println(isPalindrome(s1)); // Deve retornar true
        System.out.println(isPalindrome(s2)); // Deve retornar false
    }

}
