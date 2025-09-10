 String url = "https://partner.bajajallianz.com/payment/Paymentfailure";

        try {
            URL obj = new URL(url);
            HttpURLConnection con = (HttpURLConnection) obj.openConnection();
            con.setRequestMethod("GET");
            con.setConnectTimeout(5000); 
            con.setReadTimeout(10000);   

            int responseCode = con.getResponseCode();
            if (responseCode == HttpURLConnection.HTTP_OK) {
                try (BufferedReader in = new BufferedReader(
                        new InputStreamReader(con.getInputStream()))) {
                    String inputLine;
                    StringBuilder response = new StringBuilder();
                    while ((inputLine = in.readLine()) != null) {
                        response.append(inputLine);
                    }
                    System.out.println("Success: " + response.toString());
                }
            } else {
                System.err.println(" HTTP error: " + responseCode);
            }

        } catch (IOException e) {
            System.err.println(" Network/IO error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println(" Unexpected error: " + e.getMessage());
        }
    }
