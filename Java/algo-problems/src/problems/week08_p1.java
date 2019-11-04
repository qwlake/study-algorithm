package problems;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.Scanner;

public class week08_p1 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		while (input.hasNext()) {
			List<Champ> list = new ArrayList<>();
			int champs = Integer.parseInt(input.nextLine());
			String[] champNames =  new String[champs];
			int[][] champKDA = new int[champs][3];
			for (int i = 0; i < champs; i++) {
				String line = input.nextLine();
				champNames[i] = line.split(" ")[0];
				champKDA[i][0] = Integer.parseInt(line.split(" ")[1].split("/")[0]);
				champKDA[i][1] = Integer.parseInt(line.split(" ")[1].split("/")[1]);
				champKDA[i][2] = Integer.parseInt(line.split(" ")[1].split("/")[2]);
				if (champKDA[i][0] + champKDA[i][2] >= champKDA[i][1]) {
					list.add(new Champ(champNames[i], champKDA[i][0], champKDA[i][1], champKDA[i][2]));
				}
				Collections.sort(list, new ChampCompare());
			}
			for (Champ temp : list)
				System.out.println(temp.toString());
		}
	}
}

class Champ {
    String name;
    int k;
    int death;
    int a;
    int ka;
    double kda;
    
    Champ(String name, int k, int death, int a) {
        this.name = name;
        this.k = k;
        this.death = death;
        this.a = a;
        this.ka = k+a;
        if (death == 0) {
        	this.kda = 10000000 + ka;
        } else {
        	this.kda = ka / death;
        }
    }
    
    public String toString() {
    	return name + " " + k + "/" + death + "/" + a;
    }
}

class ChampCompare implements Comparator<Champ> {
    int ret = 0;
    
    @Override
    public int compare(Champ c1, Champ c2) {
        if(c1.kda < c2.kda) {
            ret = 1;
        }
        else if(c1.kda == c2.kda) {
            if(c1.death > c2.death) {
                ret = 1;
            } else if(c1.death == c2.death) {
            	if(c1.name.compareTo(c2.name) < 0) {
                    ret = -1;
                } else if(c1.name.compareTo(c2.name) == 0) {
                    ret = 0;
                } else if(c1.name.compareTo(c2.name) > 0) {
                    ret = 1;
                }
            } else if(c1.death < c2.death) {
                ret = -1;
            }
        }
        else if(c1.kda > c2.kda) {
            ret = -1;
        }
        return ret;
    }
}