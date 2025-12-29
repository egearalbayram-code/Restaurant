import orders

def daily_sales_report(orders_list: list) -> dict:
    total = sum(orders.calculate_bill(o, 0.1, 0.1)['total'] for o in orders_list)
    return {"revenue": total, "count": len(orders_list)}

def top_selling_items(orders_list: list, menu: dict, limit: int = 5) -> list:
    counts = {}
    for o in orders_list:
        for i in o['items']:
            counts[i['name']] = counts.get(i['name'], 0) + i['quantity']
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]

def server_performance(orders_list: list) -> dict:
    return {}

def export_report(report: dict, filename: str) -> str:
    with open(filename, 'w') as f:
        for k, v in report.items():
            f.write(f"{k}: {v}\n")
    return filename