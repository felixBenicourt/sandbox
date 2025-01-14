name = "sandbox"
version = "1.0.0"
author = "felix benicourt"

description = ""

build_command = False
requires = ['iter-1.1.0', 'python-3.10']

def commands():
    env.PYTHONPATH.append(this.root)
    env.PYTHONPATH.append("{root}\sandbox")
    env.PATH.append(this.root)
    env.PATH.append("{root}\sandbox")
    alias("warp_mysql", "python {root}/sandbox/warp_mysql.py")
    alias("ticket_id", "python {root}/sandbox/generate_ticket_id.py")
    alias("extractvector", "python {root}/sandbox/exctract_metahuman_blendshapes_ada.py")
    alias("applyDisplacement", "python {root}/sandbox/blendshape_apply_vector.py")

