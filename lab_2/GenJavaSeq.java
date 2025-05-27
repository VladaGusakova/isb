import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class GenJavaSeq {
    
    /**
    * Generates a random bit sequence
    * @param length Length of the sequence
    * @return Generated sequence
    */
    public static String generate_seq(int length) {
        StringBuilder sequence = new StringBuilder(length);
        Random random = new Random();

        for (int i = 0; i < length; i++) {
            sequence.append(random.nextBoolean() ? '1' : '0');
        }
        return sequence.toString();
    }

    /**
    * Saves a sequence to a JSON file
    * @param sequence The sequence to save
    * @param filename The file name to save
    */
    public static void save_seq(String sequence, String filename) {
        try (FileWriter writer = new FileWriter(filename)) {
            writer.write("{\n  \"sequence\": \"" + sequence + "\"\n}");
        } catch (IOException e) {
            System.err.println("Error writing file: " + e.getMessage());
        }
    }

    /**
    * Main method of the program
    * @param args Command line arguments
    */
    public static void main(String[] args) {
        String sequence = generate_seq(128);
        save_seq(sequence, "java_seq.json");
    }
}
