# Function to view goods status
def view_goods_status(port_name):
    query_ = f"SELECT g.*, s.name as ship_name FROM goods g JOIN ships s ON g.ship_id = s.ship_id WHERE s.port_name = '{port_name}'"
    display_results(query_)