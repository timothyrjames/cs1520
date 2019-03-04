import java.net.Socket;
import java.net.ServerSocket;
import java.io.*;

public class VerySimpleWebServer {

  public static void main(String[] arguments) throws Exception {

    ServerSocket serverSocket = new ServerSocket(8080);
    Socket clientConnection = null;
    do {
      clientConnection = serverSocket.accept(); // this is a blocking call
      
      // The following lines write out the text of the HTTP Request to the console.
      InputStream in = clientConnection.getInputStream();
      BufferedReader reader = new BufferedReader(new InputStreamReader(in));
      String line = reader.readLine();
      while (line != null && !line.equals("")) {
        System.out.println(line);
        line = reader.readLine();
      }

      // The following lines write a very simple HTTP response back to the client.
      OutputStreamWriter out = new OutputStreamWriter(clientConnection.getOutputStream());
      out.write("HTTP/1.1 200 OK\n");
      out.write("Content-Type: text/html; charset=utf-8\n\n");
      out.write("<html><body>THIS IS A RESPONSE</body></html>");
    
      out.close();
    
    } while (clientConnection != null);
  }
}
