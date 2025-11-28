import os

from toolbox_core import auth_methods
from toolbox_langchain import ToolboxClient

TOOLBOX_URL = os.getenv("TOOLBOX_URL", default="http://127.0.0.1:5000")


# Tools for agent
async def initialize_tools():
    # 1. เชื่อมต่อกับ Toolbox Server
    auth_token_provider = auth_methods.aget_google_id_token(TOOLBOX_URL)
    client = ToolboxClient(
        TOOLBOX_URL, client_headers={"Authorization": auth_token_provider}
    )

    # 2. โหลด Toolset
    # หมายเหตุ: ชื่อ "cymbal_air" ตรงນີ້ขึ้นอยู่ກັບไฟล์ tools.yaml ທີ່ Run ຢູ່ Server Toolbox
    # ຖ້າທ່ານຍັງບໍ່ໄດ້ປ່ຽນຊື່ໃນ tools.yaml ໃຫ້ໃຊ້ "cymbal_air" ຄືເກົ່າ
    # ມັນຈະໄປດຶງ Tool ທີ່ Auto-generate ຈາກ Database (ເຊັ່ນ: search_products) ມາໃຫ້
    tools = await client.aload_toolset("bcel_products")

    # 3. ตัดส่วน insert_ticket/validate_ticket ทิ้งไป
    # insert_ticket = await client.aload_tool("insert_ticket")
    # validate_ticket = await client.aload_tool("validate_ticket")

    # 4. Return แค່ tools list อย่างเดียว (เพื่อให้ตรงกับ agent.py)
    return tools


def get_confirmation_needing_tools():
    # ไม่มีการจองตั๋วแล้ว ไม่ต้อง confirm อะไร
    return []


def get_auth_tools():
    # การค้นหา Product ส่วนใหญ่เป็นข้อมูลสาธารณะ ไม่ต้อง Login
    # แต่ถ้าอนาคตมีดู "ยอดเงินในบัญชี" ต้องเอาชื่อ Tool มาใส่ตรงนี้
    return []