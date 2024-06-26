from molsysmt._private.digestion import digest

@digest(form='file:mmtf')
def to_molsysmt_TopologyOld(item, atom_indices='all'):

    from . import to_mmtf_MMTFDecoder
    from ..mmtf_MMTFDecoder import to_molsysmt_TopologyOld as mmtf_MMTFDecoder_to_molsysmt_TopologyOld

    tmp_item = to_mmtf_MMTFDecoder(item)
    tmp_item = mmtf_MMTFDecoder_to_molsysmt_TopologyOld(tmp_item, atom_indices=atom_indices)

    return tmp_item

