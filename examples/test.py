import sys

vinaPath = '/home/rafalb/work/vina/autodock_vina_1_1_2_linux_x86/bin'
sys.path.append(vinaPath)

sys.path.append('/home/rafalb/work/molecules/moleculeGenerator/moleculegenerator/pyscreener')
sys.path.append('/home/rafalb/ADFRsuite-1.0/bin')



from pyscreener.docking import vina
vina.Vina(software='vina', receptors=['5WIU.pdb'], center = [-18, 13.5, -17])
pass