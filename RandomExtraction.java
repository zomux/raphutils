import java.util.*;
import java.io.*;

class RandomExtraction {

    public static List<String> readlines (String filename) throws IOException {

        BufferedReader reader = new BufferedReader(new FileReader(filename));
        String line;
        List<String> results = new ArrayList<String>();
        while ((line = reader.readLine()) != null) {
            results.add(line.trim());
        }
        reader.close();
        return results;

    }

    public static List<Integer> getRandomNumbers (int maxValue, int numbers) {

        Random rand = new Random();
        List<Integer> randomValues = new ArrayList<Integer>();
        int n = 0;
        while (n < numbers) {
            int newValue = rand.nextInt(maxValue);
            if (!randomValues.contains(newValue)) {
                randomValues.add(newValue);
                n ++;
            }
        }
        return randomValues;

    }

    public static void main (String[] args) throws IOException {

        if (args.length != 3) {
            System.err.println("java [srouce] [destination] [samples-count]");
            System.exit(0);
        }

        List<String> enLines = readlines(args[0] + ".en");
        List<String> jaLines = readlines(args[0] + ".ja");

        int sampleCount = Integer.parseInt(args[2]);
        List<Integer> randomNumbers = getRandomNumbers(enLines.size(), sampleCount);

        BufferedWriter enWriter = new BufferedWriter(new FileWriter(args[1] + ".en"));
        BufferedWriter jaWriter = new BufferedWriter(new FileWriter(args[1] + ".ja"));
        for (int randomNumber : randomNumbers) {
            enWriter.write(enLines.get(randomNumber) + "\n");
            jaWriter.write(jaLines.get(randomNumber) + "\n");
        }
        enWriter.close();
        jaWriter.close();

    }

}