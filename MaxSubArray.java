public class MaxSubArray {

    public static int maxSubArray(int[] nums) {
        // Inicializa as variáveis com o primeiro elemento do array
        int maxCurrent = nums[0];
        int maxGlobal = nums[0];

        // Itera sobre o array começando do segundo elemento
        for (int i = 1; i < nums.length; i++) {
            // Atualiza maxCurrent: pega o valor atual ou começa um novo subarray
            maxCurrent = Math.max(nums[i], maxCurrent + nums[i]);

            // Se maxCurrent for maior que maxGlobal, atualiza maxGlobal
            if (maxCurrent > maxGlobal) {
                maxGlobal = maxCurrent;
            }
        }

        // Retorna a maior soma encontrada
        return maxGlobal;
    }

    public static void main(String[] args) {
        int[] nums = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println("A maior soma do array é: " + maxSubArray(nums));
    }

}