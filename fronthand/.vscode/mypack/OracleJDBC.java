import java.sql.*;

public class OracleJDBC {
    public static void main(String[] args) {
        try {
            // Step 1: Load Oracle JDBC Driver
            Class.forName("oracle.jdbc.driver.OracleDriver");

            // Step 2: Establish Connection
            Connection con = DriverManager.getConnection(
                "jdbc:oracle:thin:@localhost:1521:xe", // URL
                "system",                              // username
                "your_password"                        // password
            );

            // Step 3: Insert into table
            String insertQuery = "INSERT INTO student (id, name) VALUES (?, ?)";
            PreparedStatement pstmt = con.prepareStatement(insertQuery);
            pstmt.setInt(1, 101); // student id
            pstmt.setString(2, "Aisha"); // student name
            int inserted = pstmt.executeUpdate();
            System.out.println("Rows inserted: " + inserted);

            // Step 4: Select from table
            Statement stmt = con.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM student");

            System.out.println("Student Data:");
            while (rs.next()) {
                System.out.println(rs.getInt(1) + " " + rs.getString(2));
            }

            // Step 5: Close connection
            con.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
}
