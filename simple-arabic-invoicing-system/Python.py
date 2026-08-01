import os

# --- إعدادات النظام ---
# يجب التأكد من وجود مسار D:\Invoices أو تغييره
INVOICES_DIR = r"D:\Invoices" 
LAST_INVOICE_FILE = "last_invoice_number.txt"

def get_next_invoice_number():
    """يحصل على رقم الفاتورة التالي من الملف ويحدّثه."""
    try:
        if not os.path.exists(LAST_INVOICE_FILE):
            last_number = 0
        else:
            with open(LAST_INVOICE_FILE, 'r', encoding='utf-8') as f:
                last_number = int(f.read().strip() or 0)
    except:
        last_number = 0
        
    next_number = last_number + 1

    # تحديث رقم الفاتورة في الملف
    with open(LAST_INVOICE_FILE, 'w', encoding='utf-8') as f:
        f.write(str(next_number))
        
    return next_number

# --- 1. صنف المنتج (Product Class) ---
# لتعريف خصائص المنتج (الاسم، السعر)
class Product:
    """يمثل منتجاً واحداً (اسم المنتج، سعر البيع للوحدة)."""
    
    def __init__(self, name_ar, price):
        # الباني: تهيئة خصائص المنتج
        self.name_ar = name_ar           
        self.price = price   

# --- 2. صنف الفاتورة (Invoice Class) ---
# يحتوي على المنتجات ويحسب الإجمالي ويقوم بالحفظ
class Invoice:
    """يمثل فاتورة تحتوي على مجموعة من المنتجات."""

    def __init__(self, customer_name_ar="عميل نقدي"):
        # الباني: تهيئة خصائص الفاتورة
        self.invoice_number = get_next_invoice_number() # رقم تلقائي
        self.customer_name_ar = customer_name_ar 
        # لتخزين المنتجات (كائن المنتج، الكمية)
        self.items = []                      
        
    def add_item(self, product_obj, quantity):
        """يضيف منتجاً بكميته إلى الفاتورة."""
        if isinstance(product_obj, Product) and quantity > 0:
            # العلاقة بين الأصناف: الفاتورة (Invoice) "تحتوي على" منتجات (Product)
            self.items.append({
                'product': product_obj,
                'quantity': quantity
            })
            print(f"✅ تمت إضافة {quantity} من {product_obj.name_ar}.")
        
    def calculate_total(self):
        """يحسب الإجمالي الكلي للفاتورة."""
        total = 0
        for item in self.items:
            # سعر الوحدة * الكمية
            total += item['product'].price * item['quantity']
        return total

    def generate_content(self):
        """ينشئ نص الفاتورة للطباعة والحفظ."""
        total = self.calculate_total()
        content = f"--- 📄 فاتورة رقم: {self.invoice_number} ---\n"
        content += f"اسم العميل: {self.customer_name_ar}\n"
        content += "-" * 40 + "\n"
        content += "{:<20} {:<10} {:<10} {:<15}\n".format("المنتج", "الكمية", "السعر/وحدة", "الإجمالي")
        content += "-" * 40 + "\n"
        
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            total_price_item = product.price * quantity
            
            content += "{:<20} {:<10} {:<10.2f} {:<15.2f}\n".format(
                product.name_ar,
                quantity,
                product.price,
                total_price_item
            )
            
        content += "-" * 40 + "\n"
        content += "💰 إجمالي الفاتورة النهائي: {:.2f}\n".format(total)
        
        return content

    def save_invoice(self):
        """يحفظ محتوى الفاتورة كملف خارجي."""
        
        if not os.path.exists(INVOICES_DIR):
            try:
                os.makedirs(INVOICES_DIR)
            except Exception as e:
                print(f"❗ تعذر إنشاء مجلد الفواتير: {e}")
                return

        file_path = os.path.join(INVOICES_DIR, f"Invoice_{self.invoice_number}.txt")
        
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(self.generate_content())
            print(f"\n✅ تمت معالجة وحفظ الفاتورة رقم {self.invoice_number} بنجاح.")
            print(f"تم حفظها في: {file_path}")
            
        except Exception as e:
            print(f"❗ حدث خطأ أثناء حفظ الفاتورة: {e}")


# --- 3. بيانات المنتجات (المدخلة من المبرمج) ---

PRODUCTS_DATA = {
    "1": Product("حليب طازج", 18.50),
    "2": Product("خبز بلدي", 7.00),
    "3": Product("علبة شاي", 35.00),
    "4": Product("أرز مصري 1كجم", 48.00)
}

# --- 4. تشغيل البرنامج الرئيسي ---

def run_invoicing_program():
    """الدالة الرئيسية لتشغيل برنامج الفواتير."""
    
    print("📋 قائمة المنتجات المتاحة:")
    for key, product in PRODUCTS_DATA.items():
        print(f"🔑 المفتاح: **{key}** | المنتج: {product.name_ar} | السعر: {product.price:.2f}")
    print("-" * 50)
    
    while True:
        print("\n--- 💡 بدء فاتورة جديدة ---")
        
        current_invoice = Invoice("العميل")
        print(f"تم إنشاء الفاتورة رقم: **{current_invoice.invoice_number}**")

        # إدخال المنتجات
        while True:
            # رسائل باللغة العربية (المتطلب)
            product_key = input("أدخل مفتاح المنتج المراد إضافته، أو اكتب 'p' للطباعة/الحفظ: ").strip().lower()
            
            if product_key == 'p':
                break
                
            if product_key in PRODUCTS_DATA:
                try:
                    product_obj = PRODUCTS_DATA[product_key]
                    quantity = int(input(f"أدخل الكمية المطلوبة من {product_obj.name_ar}: "))
                    if quantity > 0:
                        current_invoice.add_item(product_obj, quantity)
                    else:
                        print("❗ يجب أن تكون الكمية أكبر من الصفر.")
                except ValueError:
                    print("❗ الكمية المدخلة غير صالحة.")
            else:
                if product_key != '':
                    print("❗ مفتاح المنتج غير موجود. يرجى الاختيار من القائمة.")

        # حفظ وعرض الفاتورة
        if current_invoice.items:
            print("\n--- تفاصيل الفاتورة ---")
            print(current_invoice.generate_content())
            current_invoice.save_invoice()
            
        else:
            print("❗ الفاتورة فارغة. لم يتم حفظها.")

        # سؤال المستخدم حول الاستمرار أو الإنهاء
        next_action = input("\nإذا كنت تريد تسجيل فاتورة أخرى، اضغط 'p'. للخروج، اكتب 'exit': ").strip().lower()
        if next_action == 'exit':
            print("👋 شكراً لك. تم إنهاء البرنامج.")
            break

if __name__ == "__main__":
    # تشغيل البرنامج
    run_invoicing_program()