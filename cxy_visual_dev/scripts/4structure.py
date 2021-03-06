import os
from os.path import join as pjoin

from numpy import inf
from cxy_visual_dev.lib.predefine import proj_dir,\
    dataset_name2info, s1200_1096_thickness, s1200_1096_myelin,\
    s1200_avg_thickness, s1200_avg_myelin
from cxy_visual_dev.lib.algo import ROI_analysis, pca,\
    ROI_analysis_on_PC, make_age_maps, calc_map_corr,\
    mask_maps, merge_by_age, vtx_corr_col, polyfit

work_dir = pjoin(proj_dir, 'analysis/structure')
if not os.path.isdir(work_dir):
    os.makedirs(work_dir)


if __name__ == '__main__':
    # HCP_MMP1 atlas 包含 Cole_visual_ROI
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness.dscalar.nii'),
    #     atlas_name='HCP_MMP1',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_HCP_MMP1.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness.dscalar.nii'),
    #     atlas_name='HCP_MMP1', zscore_flag=True,
    #     out_file=pjoin(work_dir, 'HCPD_thickness_HCP_MMP1_zscore.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness.dscalar.nii'),
    #     atlas_name='LR',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness.dscalar.nii'),
    #     atlas_name='Cole_visual_LR',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_Cole_visual_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin.dscalar.nii'),
    #     atlas_name='HCP_MMP1',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_HCP_MMP1.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin.dscalar.nii'),
    #     atlas_name='HCP_MMP1', zscore_flag=True,
    #     out_file=pjoin(work_dir, 'HCPD_myelin_HCP_MMP1_zscore.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin.dscalar.nii'),
    #     atlas_name='LR',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin.dscalar.nii'),
    #     atlas_name='Cole_visual_LR',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_Cole_visual_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness_4mm.dscalar.nii'),
    #     atlas_name='HCP_MMP1',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_4mm_HCP_MMP1.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness_4mm.dscalar.nii'),
    #     atlas_name='FFA',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_4mm_FFA.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin_4mm.dscalar.nii'),
    #     atlas_name='HCP_MMP1',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_4mm_HCP_MMP1.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin_4mm.dscalar.nii'),
    #     atlas_name='FFA',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_4mm_FFA.csv')
    # )

    # ROI_analysis(
    #     data_file=s1200_1096_thickness,
    #     atlas_name='Cole_visual_LR',
    #     out_file=pjoin(work_dir, 'HCPY_thickness_Cole_visual_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=s1200_1096_myelin,
    #     atlas_name='Cole_visual_LR',
    #     out_file=pjoin(work_dir, 'HCPY_myelin_Cole_visual_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPA_thickness.dscalar.nii'),
    #     atlas_name='Cole_visual_LR',
    #     out_file=pjoin(work_dir, 'HCPA_thickness_Cole_visual_LR.csv')
    # )
    # ROI_analysis(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPA_myelin.dscalar.nii'),
    #     atlas_name='Cole_visual_LR',
    #     out_file=pjoin(work_dir, 'HCPA_myelin_Cole_visual_LR.csv')
    # )

    # merge_by_age(
    #     data_file=pjoin(work_dir, 'HCPD_thickness_Cole_visual_LR.csv'),
    #     info_file=dataset_name2info['HCPD'],
    #     out_name=pjoin(work_dir, 'HCPD_thickness_Cole_visual_LR_merge-age')
    # )
    # merge_by_age(
    #     data_file=pjoin(work_dir, 'HCPD_myelin_Cole_visual_LR.csv'),
    #     info_file=dataset_name2info['HCPD'],
    #     out_name=pjoin(work_dir, 'HCPD_myelin_Cole_visual_LR_merge-age')
    # )

    # merge_by_age(
    #     data_file=pjoin(work_dir, 'HCPD_thickness_HCP_MMP1.csv'),
    #     info_file=dataset_name2info['HCPD'],
    #     out_name=pjoin(work_dir, 'HCPD_thickness_HCP_MMP1_merge-age')
    # )
    # merge_by_age(
    #     data_file=pjoin(work_dir, 'HCPD_myelin_HCP_MMP1.csv'),
    #     info_file=dataset_name2info['HCPD'],
    #     out_name=pjoin(work_dir, 'HCPD_myelin_HCP_MMP1_merge-age')
    # )

    # pca(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness_4mm.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     n_component=20, axis='vertex',
    #     out_name=pjoin(work_dir, 'HCPD_thickness_4mm_R_cole_visual_PCA-vtx')
    # )
    # pca(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin_4mm.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     n_component=20, axis='vertex',
    #     out_name=pjoin(work_dir, 'HCPD_myelin_4mm_R_cole_visual_PCA-vtx')
    # )
    # ROI_analysis_on_PC(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness_4mm.dscalar.nii'),
    #     pca_file=pjoin(work_dir, 'HCPD_thickness_4mm_R_cole_visual_PCA-vtx.pkl'),
    #     pc_num=1, mask_atlas='Cole_visual_LR', mask_name='R_cole_visual',
    #     roi_atlas='Cole_visual_ROI',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_4mm_R_cole_visual_PCA-vtx-PC1.csv')
    # )
    # ROI_analysis_on_PC(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin_4mm.dscalar.nii'),
    #     pca_file=pjoin(work_dir, 'HCPD_myelin_4mm_R_cole_visual_PCA-vtx.pkl'),
    #     pc_num=1, mask_atlas='Cole_visual_LR', mask_name='R_cole_visual',
    #     roi_atlas='Cole_visual_ROI',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_4mm_R_cole_visual_PCA-vtx-PC1.csv')
    # )

    # pca(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness_4mm.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     n_component=20, axis='subject',
    #     out_name=pjoin(work_dir, 'HCPD_thickness_4mm_R_cole_visual_PCA-subj')
    # )
    # pca(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin_4mm.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     n_component=20, axis='subject',
    #     out_name=pjoin(work_dir, 'HCPD_myelin_4mm_R_cole_visual_PCA-subj')
    # )

    # make_age_maps(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness.dscalar.nii'),
    #     info_file=dataset_name2info['HCPD'],
    #     out_name=pjoin(work_dir, 'HCPD_thickness_age-map')
    # )
    # make_age_maps(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin.dscalar.nii'),
    #     info_file=dataset_name2info['HCPD'],
    #     out_name=pjoin(work_dir, 'HCPD_myelin_age-map')
    # )
    # make_age_maps(
    #     data_file=s1200_1096_thickness,
    #     info_file=dataset_name2info['HCPY'],
    #     out_name=pjoin(work_dir, 'HCPY_thickness_age-map')
    # )
    # make_age_maps(
    #     data_file=s1200_1096_myelin,
    #     info_file=dataset_name2info['HCPY'],
    #     out_name=pjoin(work_dir, 'HCPY_myelin_age-map')
    # )
    # make_age_maps(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPA_thickness.dscalar.nii'),
    #     info_file=dataset_name2info['HCPA'],
    #     out_name=pjoin(work_dir, 'HCPA_thickness_age-map')
    # )
    # make_age_maps(
    #     data_file=pjoin(proj_dir, 'data/HCP/HCPA_myelin.dscalar.nii'),
    #     info_file=dataset_name2info['HCPA'],
    #     out_name=pjoin(work_dir, 'HCPA_myelin_age-map')
    # )

    # mask_maps(
    #     data_file=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 's1200_avg_thickness_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 's1200_avg_myelin_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=pjoin(work_dir, 'HCPD_thickness_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_age-map-mean_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=pjoin(work_dir, 'HCPY_thickness_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPY_thickness_age-map-mean_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=pjoin(work_dir, 'HCPA_thickness_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPA_thickness_age-map-mean_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=pjoin(work_dir, 'HCPD_myelin_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_age-map-mean_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=pjoin(work_dir, 'HCPY_myelin_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPY_myelin_age-map-mean_mask-R_cole_visual.dscalar.nii')
    # )
    # mask_maps(
    #     data_file=pjoin(work_dir, 'HCPA_myelin_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPA_myelin_age-map-mean_mask-R_cole_visual.dscalar.nii')
    # )

    # calc_map_corr(
    #     data_file1=pjoin(proj_dir, 'data/HCP/HCPD_thickness.dscalar.nii'),
    #     data_file2=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=False
    # )
    # calc_map_corr(
    #     data_file1=pjoin(proj_dir, 'data/HCP/HCPD_myelin.dscalar.nii'),
    #     data_file2=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=False
    # )
    # calc_map_corr(
    #     data_file1=s1200_1096_thickness,
    #     data_file2=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPY_thickness_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=False
    # )
    # calc_map_corr(
    #     data_file1=s1200_1096_myelin,
    #     data_file2=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPY_myelin_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=False
    # )
    # calc_map_corr(
    #     data_file1=pjoin(proj_dir, 'data/HCP/HCPA_thickness.dscalar.nii'),
    #     data_file2=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPA_thickness_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=False
    # )
    # calc_map_corr(
    #     data_file1=pjoin(proj_dir, 'data/HCP/HCPA_myelin.dscalar.nii'),
    #     data_file2=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPA_myelin_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=False
    # )

    # calc_map_corr(
    #     data_file1=pjoin(work_dir, 'HCPD_thickness_age-map-mean.dscalar.nii'),
    #     data_file2=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPD_thickness_age-map_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=True
    # )
    # calc_map_corr(
    #     data_file1=pjoin(work_dir, 'HCPD_myelin_age-map-mean.dscalar.nii'),
    #     data_file2=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPD_myelin_age-map_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=True
    # )
    # calc_map_corr(
    #     data_file1=pjoin(work_dir, 'HCPY_thickness_age-map-mean.dscalar.nii'),
    #     data_file2=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPY_thickness_age-map_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=True
    # )
    # calc_map_corr(
    #     data_file1=pjoin(work_dir, 'HCPY_myelin_age-map-mean.dscalar.nii'),
    #     data_file2=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPY_myelin_age-map_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=True
    # )
    # calc_map_corr(
    #     data_file1=pjoin(work_dir, 'HCPA_thickness_age-map-mean.dscalar.nii'),
    #     data_file2=s1200_avg_thickness,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPA_thickness_age-map_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=True
    # )
    # calc_map_corr(
    #     data_file1=pjoin(work_dir, 'HCPA_myelin_age-map-mean.dscalar.nii'),
    #     data_file2=s1200_avg_myelin,
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     out_file=pjoin(work_dir, 'HCPA_myelin_age-map_map-corr_s1200-avg_R_cole_visual.csv'),
    #     map_names2=['s1200_avg'], index=True
    # )

    # vtx_corr_col(
    #     data_file1=pjoin(work_dir, 'HCPD_thickness_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     data_file2=pjoin(work_dir, 'HCPD_thickness_Cole_visual_LR_merge-age-mean.csv'),
    #     column='R_cole_visual', idx_col=None,
    #     out_file=pjoin(work_dir, 'HCPD_thickness_R_cole_visual_merge-age_vtx-corr-col.dscalar.nii')
    # )
    # vtx_corr_col(
    #     data_file1=pjoin(work_dir, 'HCPD_myelin_age-map-mean.dscalar.nii'),
    #     atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
    #     data_file2=pjoin(work_dir, 'HCPD_myelin_Cole_visual_LR_merge-age-mean.csv'),
    #     column='R_cole_visual', idx_col=None,
    #     out_file=pjoin(work_dir, 'HCPD_myelin_R_cole_visual_merge-age_vtx-corr-col.dscalar.nii')
    # )

    polyfit(
        data_file=pjoin(proj_dir, 'data/HCP/HCPD_thickness_4mm.dscalar.nii'),
        info_file=dataset_name2info['HCPD'], deg=1,
        out_file=pjoin(work_dir, 'HCPD_thickness_4mm_linear-fit-age.dscalar.nii')
    )
    polyfit(
        data_file=pjoin(proj_dir, 'data/HCP/HCPD_myelin_4mm.dscalar.nii'),
        info_file=dataset_name2info['HCPD'], deg=1,
        out_file=pjoin(work_dir, 'HCPD_myelin_4mm_linear-fit-age.dscalar.nii')
    )
    polyfit(
        data_file=pjoin(work_dir, 'HCPD_thickness_4mm_HCP_MMP1.csv'),
        info_file=dataset_name2info['HCPD'], deg=1,
        out_file=pjoin(work_dir, 'HCPD_thickness_4mm_HCP_MMP1_linear-fit-age.csv')
    )
    polyfit(
        data_file=pjoin(work_dir, 'HCPD_myelin_4mm_HCP_MMP1.csv'),
        info_file=dataset_name2info['HCPD'], deg=1,
        out_file=pjoin(work_dir, 'HCPD_myelin_4mm_HCP_MMP1_linear-fit-age.csv')
    )

    mask_maps(
        data_file=pjoin(work_dir, 'HCPD_thickness_4mm_linear-fit-age.dscalar.nii'),
        atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
        out_file=pjoin(work_dir, 'HCPD_thickness_4mm_linear-fit-age_mask-R_cole_visual.dscalar.nii')
    )
    mask_maps(
        data_file=pjoin(work_dir, 'HCPD_myelin_4mm_linear-fit-age.dscalar.nii'),
        atlas_name='Cole_visual_LR', roi_name='R_cole_visual',
        out_file=pjoin(work_dir, 'HCPD_myelin_4mm_linear-fit-age_mask-R_cole_visual.dscalar.nii')
    )
