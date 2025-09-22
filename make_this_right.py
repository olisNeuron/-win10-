import os
import tkinter as tk


def add(path):
    path = f'{path}\\Windows 10 x64.vmx'
    if os.path.exists(path):
        print('文件存在')
        with open(path, 'r') as f:
            content = f.read()
        vhv = 'vhv.enable = "TRUE"' in content
        hyper = 'hypervisor.cpuid.v0 = "FALSE"' in content
        if vhv and hyper:
            print('文件已经是正确的')
        else:
            with open(path, 'a') as f:
                f.write('vhv.enable = "TRUE"\nhypervisor.cpuid.v0 = "FALSE"\n')
                print('文件现在是正确的')
    else:
        print('文件不存在')


def remove_vmx_lines(path):
    """
    从VMX文件中删除'vhv.enable = "TRUE"'和'hypervisor.cpuid.v0 = "FALSE"'行
    """
    path = f'{path}\\Windows 10 x64.vmx'
    if os.path.exists(path):
        print('文件存在')
        with open(path, 'r') as f:
            content = f.read()
        
        vhv = 'vhv.enable = "TRUE"' in content
        hyper = 'hypervisor.cpuid.v0 = "FALSE"' in content
        
        if not vhv and not hyper:
            print('文件中不存在要删除的行')
        else:
            # 过滤掉需要删除的行
            lines = content.splitlines(keepends=True)
            filtered_lines = []
            removed_lines = []
            
            for line in lines:
                stripped_line = line.strip()
                if stripped_line in ['vhv.enable = "TRUE"', 'hypervisor.cpuid.v0 = "FALSE"']:
                    removed_lines.append(stripped_line)
                else:
                    filtered_lines.append(line)
            
            # 将过滤后的内容写回文件
            with open(path, 'w') as f:
                f.writelines(filtered_lines)
            
            if removed_lines:
                print(f'已从VMX文件中移除行: {", ".join(removed_lines)}')
            else:
                print('未找到要删除的行')
    else:
        print('文件不存在')


GUI = tk.Tk()
GUI.title('Make this right')
GUI.geometry('300x100')
GUI.resizable(False, False)
tk.Label(GUI, text='虚拟机目录路径:').place(x=30, y=10)
path = tk.StringVar()
path_entry = tk.Entry(GUI, textvariable=path)
path_entry.place(x=110, y=10)
tk.Button(GUI, text='开启虚拟化', command=lambda: add(path.get())).place(x=60, y=40)
tk.Button(GUI, text='关闭虚拟化', command=lambda: remove_vmx_lines(path.get())).place(x=160, y=40)
GUI.mainloop()