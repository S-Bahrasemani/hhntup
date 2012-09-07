from ..mixins import *


def define_objects(tree, year):

    tree.define_collection(
            name="taus",
            prefix="tau_",
            size="tau_n",
            mix=TauFourMomentum)
    tree.define_collection(
            name="taus_EF",
            prefix="trig_EF_tau_",
            size="trig_EF_tau_n",
            mix=TauFourMomentum)
    # jet_* etc. is AntiKt4LCTopo_* in tau-perf D3PDs
    tree.define_collection(
            name="jets",
            prefix="jet_",
            size="jet_n",
            mix=FourMomentum)
    tree.define_collection(
            name="jets_EM",
            prefix="jet_AntiKt4TopoEM_",
            size="jet_AntiKt4TopoEM_n",
            mix=FourMomentum)
    tree.define_collection(
            name="truetaus",
            prefix="trueTau_",
            size="trueTau_n",
            mix=MCTauFourMomentum)
    tree.define_collection(
            name="mc",
            prefix="mc_",
            size="mc_n",
            mix=MCParticle)
    tree.define_collection(
            name="muons",
            prefix="mu_staco_",
            size="mu_staco_n")
    tree.define_collection(
            name="electrons",
            prefix="el_",
            size="el_n")
    tree.define_collection(
            name="vertices",
            prefix="vxp_",
            size="vxp_n")

    if year == 2011:
        met = 'MET_RefFinal_BDTMedium_'
    else:
        met = 'MET_RefFinal_STVF_'
    print "Using %s*" % met
    tree.define_object(
            name='MET',
            prefix=met)
