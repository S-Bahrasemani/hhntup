from rootpy.tree import TreeModel
from rootpy.vector import LorentzVector
from rootpy.types import *

class TruthTau(TreeModel):

    hadronic = BoolCol(default=False)
    nprong = IntCol(default=-1111)
    npi0 = IntCol(default=-1111)
    nneutrals = IntCol(default=-1111)
    
    fourvect = LorentzVector
    fourvect_vis = LorentzVector
    fourvect_miss = LorentzVector
    
    dR_tau_nu = FloatCol(default=-1111)
    dTheta3d_tau_nu = FloatCol(default=-1111)

reco_variables = (
    ("BDTJetScore", "F"),
    ("BDTEleScore", "F"),
    ("nPi0", "I"),
    ("pt", "F"),
    ("seedCalo_eta", "F"),
    ("seedCalo_phi", "F"),
    ("seedCalo_numTrack", "I"),
    ("charge", "I"),
)

reco_extra_variables = (
    ("seedCalo_eta_boost", "F"),
    ("seedCalo_phi_boost", "F")
)

truth_variables = (
    ("pt", "F"),
    ("m", "F"),
    ("eta", "F"),
    ("phi", "F"),
    ("vis_m", "F"),
    ("vis_eta", "F"),
    ("vis_phi", "F"),
    ("vis_Et", "F"),
    ("nProng", "I"),
    ("nPi0", "I"),
    ("charge", "I"),
)

common_variables = (
    ("matched", "I"),
    ("matched_dR", "F"),
    ("matched_collision", "B"),
)

variables = [
    ("Mvis_tau1_tau2","F"),
    ("numJets","I"),
    ("jet_AntiKt4TopoEM_matched", "VI"),
    ("jet_AntiKt4TopoEM_matched_dR", "VF"),
    ("numVertices","I"),
    ("MET","F"),
    ("MET_phi","F"),
    ("HT","F"),
    ("MMC_mass","F"),
    ("error", "B"),
    ("mu", "I"),
    ("selected", "B")
]

jet_variables = (
    ("E", "F"),
    ("pt", "F"),
    ("m", "F"),
    ("eta", "F"),
    ("phi", "F"),
    ("jvtxf", "F")
)

jet_extra_variables = (
    ("Et", "F"),
    ("eta_boost", "F"),
    ("phi_boost", "F")
)

jet_matched_variables = (
    ("matched", "B"),
    ("matched_dR", "F"),
    ("matched_pdgId", "I")
)

parton_variables = (
    ("pt", "F"),
    ("eta", "F"),
    ("phi", "F"),
    ("pdgId", "I"),
)

parton_extra_variables = (
    ("Et", "F"),
)
