package parsecsv;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

/**
 * Created by MMA on 10/17/2016.
 */
public class CSV {

    public static void main(String [] args){

        String csvFile = "train_numeric.csv";
        BufferedReader br = null;
        String line = "";
        String cvsSplitBy = ",";

        int count = 0; // keep count of how many lines are read
        int cols = 0;
        int rows = 0;

        try
        {


            br = new BufferedReader(new FileReader(csvFile));
            while ((line = br.readLine()) != null)
            {
                if (count == 0){
                    String [] headers = line.split(cvsSplitBy);
                    cols = headers.length;
                    System.out.print("Headers: ");
                    for (String columnName: headers
                         ) {
                        System.out.print(columnName + " | ");
                    }
                    System.out.println();
                    rows++;
                    count++;
                    continue;
                }

                rows++;
                count++;

                /*// use comma as separator
                String[] row = line.split(cvsSplitBy);
                //System.out.print("Row #: " + count);
                for (String element: row
                     ) {
                    System.out.print(element + " | ");

                }
                System.out.println();

                count++;*/
            }

        }
        catch (FileNotFoundException e)
        {
            e.printStackTrace();
        }
        catch (IOException e)
        {
            e.printStackTrace();
        }
        finally
        {
            if (br != null)
            {
                try
                {
                    br.close();
                }
                catch (IOException e)
                {
                    e.printStackTrace();
                }
            }
        }
        System.out.println("Done. Rows: " + rows + " Cols: " + cols);


    }
}
