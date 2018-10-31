import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class ScrapPrice {
    public static void main(String[] args)  {

        Document Doc = null;
        String ele = null;

        try {

            Doc = Jsoup.connect("https://www.amazon.in/Isopure-Carb-Protein-Isolate-Powder/dp/B000E8ZJGS/ref=lp_14524817031_1_3?s=hpc&ie=UTF8&qid=1538238414&sr=1-3").get();

        }catch (Exception e){
            System.out.println("not found............");
        }

        try {
            ele = Doc.getElementById("priceblock_ourprice").text();

        } catch (Exception e){
            ele = Doc.getElementById("priceblock_saleprice").text();
        }
        
        catch (Exception e){
            ele = Doc.getElementById("priceblock_dealprice").text();
        }
        


        ele = ele.replace(",", "");
        double z = Double.parseDouble(ele);
        System.out.println(ele);

    }}
